import { Container, Row, Col } from "react-bootstrap";

function Footer() {
  return (
    <footer>
      <Container>
        <Row>
          <Col className="text-center py-3" style={{color: "#fb81b9"}}>Copyright &copy; ProShop</Col>
        </Row>
      </Container>
    </footer>
  );
}

export default Footer;
